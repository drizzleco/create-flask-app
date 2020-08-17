# {{name}}

A Flask app with{{ ' ' }}
{%- for extra in extras %}
{{- extra + ', ' if loop.index != extras|length else 'and ' + extra -}}
{% endfor %}

---

Generated using [create-flask-app](https://github.com/drizzleco/create-flask-app)
