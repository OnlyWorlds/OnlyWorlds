## Base
- <span class="text-field" data-tooltip="Text">Id</span>: {{id}}
- <span class="text-field" data-tooltip="Text">Name</span>: {{name}}
- <span class="text-field" data-tooltip="Text">Description</span>: {{description}}
- <span class="text-field" data-tooltip="Text">Supertype</span>: {{supertype}}
- <span class="text-field" data-tooltip="Text">Subtype</span>: {{subtype}}
- <span class="text-field" data-tooltip="Text">Image_url</span>: {{image_url}}

## Locality
- <span class="string" data-tooltip="Text">Scene</span>: {{scene}}
- <span class="string" data-tooltip="Text">Activity</span>: {{activity}}
- <span class="integer" data-tooltip="Number, max: 0">Founding_date</span>: {{founding_date}}
- <span class="integer" data-tooltip="Number, max: 0">Population_size</span>: {{population_size}}
- <span class="link-field" data-tooltip="Single Location">Parent_location</span>: {{linkify parent_location}}
- <span class="multi-link-field" data-tooltip="Multi Collective">Populations</span>: {{linkify populations}}

## Culture
- <span class="string" data-tooltip="Text">Traditions</span>: {{traditions}}
- <span class="string" data-tooltip="Text">Celebrations</span>: {{celebrations}}
- <span class="link-field" data-tooltip="Single Construct">Primary_cult</span>: {{linkify primary_cult}}
- <span class="multi-link-field" data-tooltip="Multi Construct">Secondary_cults</span>: {{linkify secondary_cults}}
- <span class="multi-link-field" data-tooltip="Multi Species">Delicacies</span>: {{linkify delicacies}}

## World
- <span class="string" data-tooltip="Text">Coordinates</span>: {{coordinates}}
- <span class="multi-link-field" data-tooltip="Multi Character">Founders</span>: {{linkify founders}}

## Construction
- <span class="string" data-tooltip="Text">Logistics</span>: {{logistics}}
- <span class="string" data-tooltip="Text">Architecture</span>: {{architecture}}
- <span class="integer" data-tooltip="Number, max: 100">Construction_rate</span>: {{construction_rate}}
- <span class="multi-link-field" data-tooltip="Multi Location">Buildings</span>: {{linkify buildings}}
- <span class="multi-link-field" data-tooltip="Multi Construct">Building_expertise</span>: {{linkify building_expertise}}

## Production
- <span class="string" data-tooltip="Text">Extraction</span>: {{extraction}}
- <span class="string" data-tooltip="Text">Industry</span>: {{industry}}
- <span class="integer" data-tooltip="Number, max: 0">Extraction_output</span>: {{extraction_output}}
- <span class="integer" data-tooltip="Number, max: 0">Industry_output</span>: {{industry_output}}
- <span class="link-field" data-tooltip="Single Construct">Primary_resource</span>: {{linkify primary_resource}}
- <span class="link-field" data-tooltip="Single Construct">Primary_industry</span>: {{linkify primary_industry}}
- <span class="multi-link-field" data-tooltip="Multi Construct">Secondary_resources</span>: {{linkify secondary_resources}}
- <span class="multi-link-field" data-tooltip="Multi Construct">Secondary_industries</span>: {{linkify secondary_industries}}

## Commerce
- <span class="string" data-tooltip="Text">Trade</span>: {{trade}}
- <span class="string" data-tooltip="Text">Infrastructure</span>: {{infrastructure}}
- <span class="string" data-tooltip="Text">Currency</span>: {{currency}}
- <span class="link-field" data-tooltip="Single Location">Primary_extraction_market</span>: {{linkify primary_extraction_market}}
- <span class="link-field" data-tooltip="Single Location">Primary_industry_market</span>: {{linkify primary_industry_market}}
- <span class="multi-link-field" data-tooltip="Multi Location">Secondary_extraction_markets</span>: {{linkify secondary_extraction_markets}}
- <span class="multi-link-field" data-tooltip="Multi Location">Secondary_industry_markets</span>: {{linkify secondary_industry_markets}}

## Localpolitics
- <span class="string" data-tooltip="Text">Government</span>: {{government}}
- <span class="string" data-tooltip="Text">Opposition</span>: {{opposition}}
- <span class="link-field" data-tooltip="Single Title">Governing_title</span>: {{linkify governing_title}}
- <span class="link-field" data-tooltip="Single Institution">Primary_faction</span>: {{linkify primary_faction}}
- <span class="multi-link-field" data-tooltip="Multi Institution">Secondary_factions</span>: {{linkify secondary_factions}}

## Regionalpolitics
- <span class="string" data-tooltip="Text">Territorial_policies</span>: {{territorial_policies}}
- <span class="link-field" data-tooltip="Single Territory">Territory</span>: {{linkify territory}}
- <span class="link-field" data-tooltip="Single Location">Rival</span>: {{linkify rival}}
- <span class="link-field" data-tooltip="Single Location">Friend</span>: {{linkify friend}}
- <span class="multi-link-field" data-tooltip="Multi Location">Soft_influence_on</span>: {{linkify soft_influence_on}}
- <span class="multi-link-field" data-tooltip="Multi Location">Hard_influence_on</span>: {{linkify hard_influence_on}}

## Strategics
- <span class="string" data-tooltip="Text">Defensibility</span>: {{defensibility}}
- <span class="integer" data-tooltip="Number, max: 0">Height</span>: {{height}}
- <span class="link-field" data-tooltip="Single Institution">Primary_fighter</span>: {{linkify primary_fighter}}
- <span class="multi-link-field" data-tooltip="Multi Institution">Secondary_fighters</span>: {{linkify secondary_fighters}}
- <span class="multi-link-field" data-tooltip="Multi Location">Defenses</span>: {{linkify defenses}}
- <span class="multi-link-field" data-tooltip="Multi Object">Fortifications</span>: {{linkify fortifications}}

