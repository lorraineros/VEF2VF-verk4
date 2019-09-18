{% extends "base.html" %}

{% block title %} {{ frett[1] }} {% endblock %}

{% block content %}
     <div class="group">
        <section class="col1">
            <h3>{{ frett[1] }}</h3>
            <img src='/static/mynd{{ frett[0] }}.png/'>
            <br>
            <br>
        </section>
        <section class="col1">
            <br>
            <br>
            <p>{{ frett[2] }}</p>
            <h5>{{ frett[3] }}</h5>
             <h5><a href="/">Forsíða</a></h5>
        </section>
     </div>
{% endblock content %}