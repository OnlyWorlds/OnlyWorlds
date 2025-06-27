using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Law : Element
{
    [JsonProperty("declaration"), TextAttribute("")]
    public string declaration;
    [JsonProperty("purpose"), TextAttribute("")]
    public string purpose;
    [JsonProperty("date"), Integer(0)]
    public int date;
    [JsonProperty("parent_law"), ReferenceAttribute(typeof(Law))]
    public string parentLaw;
    [JsonProperty("penalties"), ReferenceAttribute(typeof(Construct), true)]
    public string penalties;
    [JsonProperty("author"), ReferenceAttribute(typeof(Institution))]
    public string author;
    [JsonProperty("locations"), ReferenceAttribute(typeof(Location), true)]
    public string locations;
    [JsonProperty("zones"), ReferenceAttribute(typeof(Zone), true)]
    public string zones;
    [JsonProperty("prohibitions"), ReferenceAttribute(typeof(Construct), true)]
    public string prohibitions;
    [JsonProperty("adjudicators"), ReferenceAttribute(typeof(Title), true)]
    public string adjudicators;
    [JsonProperty("enforcers"), ReferenceAttribute(typeof(Title), true)]
    public string enforcers;
}
