# Documentation

### 1. Updating Text and Images in the Featured Image Carousel

To update the featured image carousel on the homepage:

1. **Locate the `Home.liquid` file**:
   - Path: `includes/layouts/home.liquid`

2. **Change Text**:
   - Find the `text-content` class and modify the text as needed.

3. **Change Images**:
   - Follow these steps:
     1. Upload the new image to the `assets/img/feature-img` directory.
     2. Update the image title and extension in the `data/slide-show.yml` file.

![Featured Image Tutorial]({{site.url}}{{site.baseurl}}/featured-image-tutorial.png)

---

### 2. Adding Blog Posts

To add a new blog post:

1. **Find the Blog Folder**:
   - Path: `posts`

2. **Add Images to a Blog Post**:
   - Use the following format to add images:
     ```markdown
     ![alt text]({{ site.url }}{{ site.baseurl }}/assets/img/blog-img/Screen Shot 2020-07-07 at 11.53.25 AM.png)
     ```

---

### 3. Editing the "Terms of Service and Privacy Policy" Files

To edit the "Terms of Service" and "Privacy Policy" documents:

- **Locate the Files**:
  - Path: `pages`

![Terms and Privacy Policy]({{site.url}}{{site.baseurl}}/terms-and-privacy.png)

---

### 4. Changing the Website Title, Description, Logo, and Favicon

To update the website's title, description, logo, or favicon:

- **Find and Modify the Tags**:
  - Path: `config.yml`
  - Update the respective tags accordingly.
