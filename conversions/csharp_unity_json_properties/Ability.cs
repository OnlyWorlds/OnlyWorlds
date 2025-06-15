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
    [JsonProperty("source"), ReferenceAttribute(typeof(Phenomenon))]
    public string source;
    [JsonProperty("talents"), ReferenceAttribute(typeof(Trait), true)]
    public string talents;
    [JsonProperty("instruments"), ReferenceAttribute(typeof(Object), true)]
    public string instruments;
    [JsonProperty("prerequisites"), ReferenceAttribute(typeof(Construct), true)]
    public string prerequisites;
    [JsonProperty("prevalence"), TextAttribute("")]
    public string prevalence;
    [JsonProperty("tradition"), ReferenceAttribute(typeof(Construct))]
    public string tradition;
    [JsonProperty("locus"), ReferenceAttribute(typeof(Location))]
    public string locus;
}
