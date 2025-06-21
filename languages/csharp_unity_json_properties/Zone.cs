using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Zone : Element
{
    [JsonProperty("function"), TextAttribute("")]
    public string function;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("claimed_by"), ReferenceAttribute(typeof(Institution), true)]
    public string claimedBy;
    [JsonProperty("roamed_by"), ReferenceAttribute(typeof(Creature), true)]
    public string roamedBy;
    [JsonProperty("titles"), ReferenceAttribute(typeof(Title), true)]
    public string titles;
}
