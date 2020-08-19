# {{name}}

A Flask app {{ 'with ' if extras }}
{%- if extras|length == 1 %}
{{- extras[0] }}
{%- else %}
{%- for extra in extras %}
{{- extra + ', ' if loop.index != extras|length else 'and ' + extra -}}
{% endfor %}
{%- endif %}

# Getting Started

## `make install`

- install dependencies

## `make start`

- start flask server

## `make lint`

- lint code with black
  {% if extras_includes('test') %}

## `make test`

- run tox and pytest to test code
  {% endif %}

---

Generated using [create-flask-app](https://github.com/drizzleco/create-flask-app)
