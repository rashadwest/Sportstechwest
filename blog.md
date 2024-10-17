---
layout: page
title: Interesting Blogs to Read
permalink: /blogs
excluded: true
tags: [Blogs]
---

<style>
  {% include custom.css %}
</style>

<div class="posts">
  {% for post in paginator.posts %}
    <div class="post-teaser">
        {% if post.thumbnail %}
        <div class="post-img">
            <a aria-label="{{ post.title }}" href="{{ post.url | relative_url }}">
                <img alt="{{ post.title }}" src="{{ post.thumbnail | relative_url }}">
            </a>
        </div>
        {% endif %}
        <div id="content">
          <header>
            <h1>
              <a aria-label="{{ post.title }}" class="post-link" href="{{ post.url | relative_url }}">
                {{ post.title }}
              </a>
            </h1>
            {% include blog/post_info.liquid author=post.author date=post.date %}
          </header>
          {% if site.excerpt or site.theme_settings.excerpt %}
              <div class="excerpt">
                  {% if site.excerpt == "truncate" %}
                     {{ post.content | strip_html | truncate: '250' | escape }}
                  {% else %}
                     {{ post.content | strip_html | truncate: '250' | escape }}
                  {% endif %}
              </div>
          {% endif %}
        </div>
    </div>
  {% endfor %}
</div>


