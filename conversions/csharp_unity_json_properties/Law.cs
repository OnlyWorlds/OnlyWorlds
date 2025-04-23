using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Law : Element
{
    [JsonProperty("decree"), TextAttribute("")]
    public string decree;
    [JsonProperty("date"), Integer(0)]
    public int date;
    [JsonProperty("purpose"), TextAttribute("")]
    public string purpose;
    [JsonProperty("author"), ReferenceAttribute(typeof(Institution))]
    public string author;
    [JsonProperty("jurisdictions"), ReferenceAttribute(typeof(Location), true)]
    public string jurisdictions;
    [JsonProperty("prohibitions"), ReferenceAttribute(typeof(Construct), true)]
    public string prohibitions;
    [JsonProperty("penalties"), ReferenceAttribute(typeof(Construct), true)]
    public string penalties;
    [JsonProperty("adjudicators"), ReferenceAttribute(typeof(Title), true)]
    public string adjudicators;
    [JsonProperty("enforcers"), ReferenceAttribute(typeof(Title), true)]
    public string enforcers;
}
