# Adds native lazy loading to images so pages only download pictures as the
# reader scrolls to them. The first few images on a page (logo, hero, post
# thumbnail) are left alone so above-the-fold content still loads right away.
module LazyImages
  EAGER_IMAGES = 3

  def self.process(doc)
    return unless doc.output_ext == ".html" && doc.output

    count = 0
    doc.output = doc.output.gsub(/<img\b[^>]*>/i) do |tag|
      count += 1
      next tag if count <= EAGER_IMAGES || tag =~ /\sloading\s*=/i

      tag.sub(/<img\b/i, '<img loading="lazy" decoding="async"')
    end
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  LazyImages.process(doc)
end
