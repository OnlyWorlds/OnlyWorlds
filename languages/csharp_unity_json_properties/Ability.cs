using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Ability : Element
{
    [JsonProperty("usage"), TextAttribute("")]
    public string usage;
    [JsonProperty("range"), Integer(0)]
    public int range;
    [JsonProperty("strength"), Integer(100)]
    public int strength;
    [JsonProperty("effects"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string effects;
    [JsonProperty("utility"), ReferenceAttribute(typeof(Construct), true)]
    public string utility;
    [JsonProperty("difficulty"), TextAttribute("")]
    public string difficulty;
    [JsonProperty("talent"), ReferenceAttribute(typeof(Trait), true)]
    public string talent;
    [JsonProperty("enablers"), ReferenceAttribute(typeof(Object), true)]
    public string enablers;
    [JsonProperty("requirements"), ReferenceAttribute(typeof(Construct), true)]
    public string requirements;
    [JsonProperty("prevalence"), TextAttribute("")]
    public string prevalence;
    [JsonProperty("system"), ReferenceAttribute(typeof(Phenomenon))]
    public string system;
    [JsonProperty("construct"), ReferenceAttribute(typeof(Construct))]
    public string construct;
}
