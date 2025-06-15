using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Territory : Element
{
    [JsonProperty("terrain"), TextAttribute("")]
    public string terrain;
    [JsonProperty("size"), Integer(0)]
    public int size;
    [JsonProperty("parent_territory"), ReferenceAttribute(typeof(Territory))]
    public string parentTerritory;
    [JsonProperty("maintenance"), TextAttribute("")]
    public string maintenance;
    [JsonProperty("primary_output"), Integer(0)]
    public int primaryOutput;
    [JsonProperty("secondary_output"), Integer(0)]
    public int secondaryOutput;
    [JsonProperty("primary_resource"), ReferenceAttribute(typeof(Construct))]
    public string primaryResource;
    [JsonProperty("secondary_resources"), ReferenceAttribute(typeof(Construct), true)]
    public string secondaryResources;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("occupants"), ReferenceAttribute(typeof(Species), true)]
    public string occupants;
    [JsonProperty("occurrences"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string occurrences;
}
