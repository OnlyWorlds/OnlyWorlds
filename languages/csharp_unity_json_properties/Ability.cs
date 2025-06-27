using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Ability : Element
{
    [JsonProperty("activation"), TextAttribute("")]
    public string activation;
    [JsonProperty("duration"), Integer(0)]
    public int duration;
    [JsonProperty("potency"), Integer(100)]
    public int potency;
    [JsonProperty("range"), Integer(0)]
    public int range;
    [JsonProperty("effects"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string effects;
    [JsonProperty("challenges"), TextAttribute("")]
    public string challenges;
    [JsonProperty("talents"), ReferenceAttribute(typeof(Trait), true)]
    public string talents;
    [JsonProperty("requisites"), ReferenceAttribute(typeof(Construct), true)]
    public string requisites;
    [JsonProperty("prevalence"), TextAttribute("")]
    public string prevalence;
    [JsonProperty("tradition"), ReferenceAttribute(typeof(Construct))]
    public string tradition;
    [JsonProperty("source"), ReferenceAttribute(typeof(Phenomenon))]
    public string source;
    [JsonProperty("locus"), ReferenceAttribute(typeof(Location))]
    public string locus;
    [JsonProperty("instruments"), ReferenceAttribute(typeof(Object), true)]
    public string instruments;
    [JsonProperty("systems"), ReferenceAttribute(typeof(Construct), true)]
    public string systems;
}
