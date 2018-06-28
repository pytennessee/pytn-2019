require 'liquid'

module Sponsors
  def tiered_sponsors(sponsors, tiers)
    grouped_sponsors = sponsors.group_by { |s| s['tier'] }
    sorted_sponsors = grouped_sponsors.sort_by { |t| tiers.index(t[0]) }
    return sorted_sponsors
  end
end

Liquid::Template.register_filter(Sponsors)
