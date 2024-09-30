import dataclasses
import io
from typing import Any, Dict, Optional
import re
import unicodedata
from logging import warn
import yaml
from docutils import nodes
from docutils.nodes import Node
from sphinx.writers.latex import LaTeXTranslator
from sphinx_proof.nodes import (  # type: ignore
    find_parent,
    latex_admonition_start,
    definition_node,
    depart_enumerable_node,
)
from sphinx.domains.index import IndexRole


translations: Dict[str, str] = {}


def _(s: str) -> str:
    return translations.get(s, s)


ref_pattern = re.compile("(.*) *<(.*)>")


def normalize_ref(text: str) -> str:
    """
    Normalize text to a reference

    Strip; lower case; replaces spacing by single spaces

    Example:

        >>> normalize_ref("Écrire	à l'envers")
        "écrire à l'envers"
    """
    text = text.strip()
    text = text.lower()
    return re.sub(r"\s+", " ", text)


def myst_ref(text: str) -> str:
    """
    Normalize text to a valid myst ref

    Like normalize_ref, but replaces spaces and `'` by `_` and remove accents.

    Example:

        >>> myst_ref("Écrire	à l'envers")
        'ecrire_a_l_envers'
    """
    text = normalize_ref(text)
    text = re.sub(r"\s+|'", "_", text)
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')


config = yaml.safe_load(io.open("_config.yml"))
semantic = config.get("semantic", {})
namespace = semantic.get("namespace")


@dataclasses.dataclass
class Symbol:
    verbalization: str
    en: Optional[str] = None
    mathhub: Optional[str] = None
    wikidata: Optional[str] = None
    depends_on: Optional[Any] = None

    def uri(self):
        """
        Return a URI for that symbol

        >>> Symbol(verbalization='foo',
        ...        mathhub='[smglom/computing]mod?program?program').uri()
        'https://mathhub.org/smglom/computing/program?program'

        >>> Symbol(verbalization='foo').uri()
        'https://Nicolas.Thiery.name/Enseignement/Info111?foo'
        """
        if self.mathhub is not None:
            return "https://mathhub.org" + self.mathhub.replace("[", "/").replace("]mod?", "/")
        return self.verbalization_uri()

    def verbalization_uri(self):
        """
        Return the verbalization URI for that symbol

        (a URI for how it's named in this particular document)

        Example:

        >>> Symbol(verbalization='foo bar').verbalization_uri()
        'https://Nicolas.Thiery.name/Enseignement/Info111?foo bar'
        """
        return semantic['namespace'] + "?" + self.verbalization


symbols = {
    normalize_ref(c['verbalization']): Symbol(**c)
    for c in semantic.get("symdecls", [])
}


class SpanNode(nodes.Element):
    pass


def visit_span_node(self, node):
    self.body.append(self.starttag(node, "span", **node.attributes))


def depart_span_node(self, node):
    self.body.append("</span>")


def noop(self, node):
    pass


index_role = IndexRole()


def definiendum_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    mynodes = []
    if "Devoirs" in inliner.document.current_source:
        index, target, _ = index_role(name, rawtext, text, lineno, inliner)[0]
        mynodes += [index, target]
    res = re.match(ref_pattern, text)
    if res:
        text = res.group(1).rstrip()
        ref = res.group(2)
    else:
        ref = text
    ref = normalize_ref(ref)
    # text = nodes.emphasis(text, text)
    if ref in symbols:
        symbol = symbols[ref]
    else:
        warn(f"Symbol unknown: {ref}")
        symbol = Symbol(verbalization=ref)
    node = SpanNode(**{"shtml:definiendum": symbol.uri(),
                       "shtml:definiendum:verbalization": symbol.verbalization_uri()})
    node += nodes.strong(text, text)
    mynodes += [node]
    return mynodes, []


def symref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    res = re.match(ref_pattern, text)
    if res:
        text = res.group(1).rstrip()
        ref = res.group(2)
    else:
        ref = normalize_ref(text)
    node = SpanNode(**{"shtml:term": "OMID", "shtml:head": ref})
    node += nodes.Text(text)
    return [node], []


def usemodule_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = SpanNode(**{"shtml:usemodule": text, "style": "display:none"})
    return [node], []


def importmodule_role(
    name, rawtext, text: str, lineno, inliner, options={}, content=[]
):
    if text.endswith(".md"):
        text = text[:-3] + ".html"
    node = SpanNode(**{"shtml:importmodule": text, "style": "display:none"})
    return [node], []


# taken from sphinx-proof/sphinx_proof/nodes.py
def visit_enumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        docname = find_parent(self.builder.env, node, "section")
        self.body.append("\\label{" + f"{docname}:{node.attributes['label']}" + "}")
        self.body.append(latex_admonition_start)
    else:
        self.body.append(
            self.starttag(node, "div", CLASS="admonition", **{"shtml:definition": ""})
        )


def setup(app):
    app.add_node(SpanNode, html=(visit_span_node, depart_span_node), latex=(noop, noop))
    app.add_role("definiendum", definiendum_role)
    app.add_role("symref", symref_role)
    app.add_role("usemodule", usemodule_role)
    app.add_role("importmodule", importmodule_role)

    app.setup_extension("sphinx_proof")
    app.add_enumerable_node(
        definition_node,
        "definition",
        None,
        html=(visit_enumerable_node, depart_enumerable_node),
        latex=(visit_enumerable_node, depart_enumerable_node),
        override=True,
    )

    return {"parallel_read_safe": True, "parallel_write_safe": True}

print(symbols)
