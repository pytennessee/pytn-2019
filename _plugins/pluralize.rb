require 'liquid'

module Pluralize
  def pluralize(quantity, singular, plural = nil)
    quantity = quantity.to_i
    if quantity == 1
      return singular
    elsif plural.nil?
      return "#{singular}s"
    else
      return plural
    end
  end
end

Liquid::Template.register_filter(Pluralize)
