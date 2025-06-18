using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Institution : Element
{
    [JsonProperty("doctrine"), TextAttribute("")]
    public string doctrine;
    [JsonProperty("founding_date"), Integer(0)]
    public int foundingDate;
    [JsonProperty("parent_institution"), ReferenceAttribute(typeof(Institution))]
    public string parentInstitution;
    [JsonProperty("legislation"), ReferenceAttribute(typeof(Law), true)]
    public string legislation;
    [JsonProperty("zones"), ReferenceAttribute(typeof(Zone), true)]
    public string zones;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("allies"), ReferenceAttribute(typeof(Institution), true)]
    public string allies;
    [JsonProperty("adversaries"), ReferenceAttribute(typeof(Institution), true)]
    public string adversaries;
    [JsonProperty("constructs"), ReferenceAttribute(typeof(Construct), true)]
    public string constructs;
}
