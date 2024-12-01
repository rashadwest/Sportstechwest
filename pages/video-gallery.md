---
layout: page
title: Gallery
subtitle: From the Video Gallery folder
permalink: /video-gallery
feature-img: "assets/img/header/Screenshot 2024-11-03 143947.png"
thumbnail: "assets/img/header/Screenshot 2024-11-03 143947.png"
image-gallery: "assets/img/image-gallery"
excluded: true
tags: [Video Gallery]
---


{% include gallery.html gallery_path=page.image-gallery %}

<script>
    const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

const images = document.querySelectorAll('.post-content img')
images.forEach(image => {
  image.addEventListener('click', e => {
    lightbox.classList.add('active')
    const img = document.createElement('img')
    img.src = image.src
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild)
    }
    lightbox.appendChild(img)
  })
})

lightbox.addEventListener('click', e => {
  if (e.target !== e.currentTarget) return
  lightbox.classList.remove('active')
})
</script>