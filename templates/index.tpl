{% extends "base.html" %}

{% block title %} This is cat news  {% endblock %}

{% block head %}
    {{ super() }}
<style type="text/css">
    .important {color: #369;}
</style>
{% endblock %}

{% block content %}
    <div class=" " " " >
        <section class="top2em">
            <h1>This is cat news</h1>
            <ul>
                {% for item in frettir %}
                    <li><a href='/frett/{{ item[0] }}'>{{ item[1] }}</a> </li>
                {% endfor %}
            </ul>
        </section>
    </div>
{% endblock %}