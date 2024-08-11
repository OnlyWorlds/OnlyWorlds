## Base
- <span class="text-field" data-tooltip="Text">Id</span>: {{id}}
- <span class="text-field" data-tooltip="Text">Name</span>: {{name}}
- <span class="text-field" data-tooltip="Text">Description</span>: {{description}}
- <span class="text-field" data-tooltip="Text">Supertype</span>: {{supertype}}
- <span class="text-field" data-tooltip="Text">Subtype</span>: {{subtype}}
- <span class="text-field" data-tooltip="Text">Image_url</span>: {{image_url}}

## Situation
- <span class="string" data-tooltip="Text">Terrain</span>: {{terrain}}
- <span class="integer" data-tooltip="Number, max: 0">Size</span>: {{size}}
- <span class="link-field" data-tooltip="Single Territory">Parent_territory</span>: {{linkify parent_territory}}

## Yield
- <span class="string" data-tooltip="Text">Maintenance</span>: {{maintenance}}
- <span class="integer" data-tooltip="Number, max: 0">Primary_output</span>: {{primary_output}}
- <span class="integer" data-tooltip="Number, max: 0">Secondary_output</span>: {{secondary_output}}
- <span class="link-field" data-tooltip="Single Construct">Primary_resource</span>: {{linkify primary_resource}}
- <span class="multi-link-field" data-tooltip="Multi Construct">Secondary_resources</span>: {{linkify secondary_resources}}

## World
- <span class="string" data-tooltip="Text">History</span>: {{history}}
- <span class="multi-link-field" data-tooltip="Multi Species">Occupants</span>: {{linkify occupants}}
- <span class="multi-link-field" data-tooltip="Multi Phenomenon">Occurrences</span>: {{linkify occurrences}}

