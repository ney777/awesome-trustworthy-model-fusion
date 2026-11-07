"""Generate a configuration-level evidence view from optional catalogue records."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import quote, urlsplit

from library import ROOT, SOURCE


def cell(value):
    """Preserve supplied evidence while keeping it inside one Markdown cell."""
    if value is None or value == "":
        return "Not recorded"
    if isinstance(value, (dict, list)):
        value = json.dumps(value, ensure_ascii=False)
    return html.escape(str(value), quote=False).replace("|", r"\|").replace("\n", "<br>")


def link(label, url):
    if not url:
        return cell(label)
    if urlsplit(url).scheme not in {"http", "https"}:
        raise ValueError("Evidence links must use http or https: " + str(url))
    return "[{}]({})".format(cell(label), quote(url, safe="/:?=#&%+~._-"))


def configurations(papers):
    """Do not infer configurations from other, differently structured fields."""
    rows = []
    seen = set()
    for paper in papers:
        entries = paper.get("model_configurations", [])
        if not isinstance(entries, list):
            raise ValueError("model_configurations must be a list: " + paper["id"])
        for config in entries:
            if not isinstance(config, dict) or not config.get("configuration_id"):
                raise ValueError("Each configuration needs configuration_id: " + paper["id"])
            key = (paper["id"], config["configuration_id"])
            if key in seen:
                raise ValueError("Duplicate configuration: " + repr(key))
            seen.add(key)
            rows.append((paper, config))
    return rows


def configuration_label(paper, config):
    return "<br>".join([
        link(paper["id"], paper.get("official_url")),
        cell(config["configuration_id"]),
        cell(config.get("label")),
    ])


def render(papers):
    rows = configurations(papers)
    paper_count = len({paper["id"] for paper, _ in rows})
    lines = [
        "# Model conditions in selected evaluated configurations",
        "",
        "This evidence view covers representative configurations with explicit catalogue records; "
        "it is not a census of all papers or experiments. The two tables refer to the same configuration IDs. "
        "Source, target and auxiliary roles remain separate.",
        "",
        "NR means a value was not reported or was not extracted; consult the parameter evidence for the reason. "
        "NR is never zero. N/A denotes an inapplicable role or parameter-count concept. "
        "Reported model-size labels are preserved without estimating missing counts from architecture names.",
        "",
        "Separate runs within a paper must not be read as a single fused model. "
        "Some evidence records explicitly group alternative students or compatible base families; "
        "their stated separation is retained. These records are unsuitable for mutually exclusive model-family statistics.",
        "",
        "Coverage: {} papers; {} configuration evidence records. Generated from optional "
        "`model_configurations` entries in `data/papers.json`.".format(paper_count, len(rows)),
        "",
        "## Roles and scale",
        "",
        "| Configuration | Source models | Target model or system | Auxiliary models |",
        "| --- | --- | --- | --- |",
    ]
    for paper, config in rows:
        lines.append("| {} | {} | {} | {} |".format(
            configuration_label(paper, config),
            cell(config.get("source_models")),
            cell(config.get("target_model")),
            cell(config.get("auxiliary_models")),
        ))
    if not rows:
        lines.append("| No configuration records available | Not recorded | Not recorded | Not recorded |")
    lines += [
        "",
        "## Interfaces and evidence",
        "",
        "| Configuration | Output paradigm | Compatibility | Parameter evidence | Source and locator |",
        "| --- | --- | --- | --- | --- |",
    ]
    for paper, config in rows:
        evidence = link("Primary source", config.get("evidence_url")) if config.get("evidence_url") else "Not recorded"
        evidence += "<br>" + cell(config.get("locator"))
        lines.append("| {} | {} | {} | {} | {} |".format(
            configuration_label(paper, config),
            cell(config.get("output_paradigm")),
            cell(config.get("compatibility")),
            cell(config.get("parameter_evidence")),
            evidence,
        ))
    if not rows:
        lines.append("| No configuration records available | Not recorded | Not recorded | Not recorded | Not recorded |")
    return "\n".join(lines) + "\n"


def generate(source=SOURCE, output=ROOT / "docs/model-conditions.md"):
    source, output = Path(source), Path(output)
    data = json.loads(source.read_text(encoding="utf-8"))
    content = render(data["papers"])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/model-conditions.md")
    args = parser.parse_args()
    print(generate(args.source, args.output))


if __name__ == "__main__":
    main()
