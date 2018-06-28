require 'liquid'

module TitleCase
  def title_case(text)
    return text.split(' ').map(&:capitalize).join(' ')
  end
end

Liquid::Template.register_filter(TitleCase)
