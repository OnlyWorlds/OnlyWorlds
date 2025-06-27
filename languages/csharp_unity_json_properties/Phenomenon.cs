using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Phenomenon : Element
{
    [JsonProperty("expression"), TextAttribute("")]
    public string expression;
    [JsonProperty("effects"), TextAttribute("")]
    public string effects;
    [JsonProperty("duration"), Integer(0)]
    public int duration;
    [JsonProperty("catalysts"), ReferenceAttribute(typeof(Object), true)]
    public string catalysts;
    [JsonProperty("empowerments"), ReferenceAttribute(typeof(Ability), true)]
    public string empowerments;
    [JsonProperty("mythology"), TextAttribute("")]
    public string mythology;
    [JsonProperty("system"), ReferenceAttribute(typeof(Phenomenon))]
    public string system;
    [JsonProperty("triggers"), ReferenceAttribute(typeof(Construct), true)]
    public string triggers;
    [JsonProperty("wielders"), ReferenceAttribute(typeof(Character), true)]
    public string wielders;
    [JsonProperty("environments"), ReferenceAttribute(typeof(Location), true)]
    public string environments;
}
