using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Phenomenon : Element
{
    [JsonProperty("presence"), TextAttribute("")]
    public string presence;
    [JsonProperty("scope"), TextAttribute("")]
    public string scope;
    [JsonProperty("duration"), Integer(0)]
    public int duration;
    [JsonProperty("intensity"), TextAttribute("")]
    public string intensity;
    [JsonProperty("empowerments"), ReferenceAttribute(typeof(Trait), true)]
    public string empowerments;
    [JsonProperty("environments"), ReferenceAttribute(typeof(Location), true)]
    public string environments;
    [JsonProperty("carriers"), ReferenceAttribute(typeof(Species), true)]
    public string carriers;
    [JsonProperty("effect"), TextAttribute("")]
    public string effect;
    [JsonProperty("catalysts"), ReferenceAttribute(typeof(Object))]
    public string catalysts;
    [JsonProperty("wielders"), ReferenceAttribute(typeof(Character), true)]
    public string wielders;
    [JsonProperty("handlers"), ReferenceAttribute(typeof(Institution), true)]
    public string handlers;
    [JsonProperty("enablers"), ReferenceAttribute(typeof(Character), true)]
    public string enablers;
    [JsonProperty("triggers"), ReferenceAttribute(typeof(Construct), true)]
    public string triggers;
    [JsonProperty("affinity"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string affinity;
}
