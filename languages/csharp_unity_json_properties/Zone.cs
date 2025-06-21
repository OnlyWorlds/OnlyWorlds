using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Zone : Element
{
    [JsonProperty("role"), TextAttribute("")]
    public string role;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
    [JsonProperty("linked_zones"), ReferenceAttribute(typeof(Zone), true)]
    public string linkedZones;
    [JsonProperty("context"), TextAttribute("")]
    public string context;
    [JsonProperty("populations"), ReferenceAttribute(typeof(Collective), true)]
    public string populations;
    [JsonProperty("titles"), ReferenceAttribute(typeof(Title), true)]
    public string titles;
    [JsonProperty("principles"), ReferenceAttribute(typeof(Construct), true)]
    public string principles;
}
