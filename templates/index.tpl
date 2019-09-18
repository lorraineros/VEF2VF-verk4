{% extends "base.html" %}

{% block title %} This is my project  {% endblock %}

{% block head %}
    {{ super() }}
<style type="text/css">
    .important {color: #369;}
</style>
{% endblock %}

{% block content %}
    <div class="group" >
        <section class="col1">
            <h3 class="important">{{frettir[0][1]}}</h3>
            <img src="/static/mynd0.png">
            <br>
            <br>
        </section>
        
        <section class="col1">
            <h3>This is my project</h3>
            <ul>
                {% for item in frettir %}
                    <li><a href='/frett/{{ item[0] }}'>{{ item[1] }}</a> </li>
                {% endfor %}
            </ul>
        </section>
    </div>
{% endblock %}