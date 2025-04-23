using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Institution : Element
{
    [JsonProperty("premise"), TextAttribute("")]
    public string premise;
    [JsonProperty("found_date"), Integer(0)]
    public int foundDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("parent_institution"), ReferenceAttribute(typeof(Institution))]
    public string parentInstitution;
    [JsonProperty("territories"), ReferenceAttribute(typeof(Territory), true)]
    public string territories;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("legal"), ReferenceAttribute(typeof(Law), true)]
    public string legal;
    [JsonProperty("situation"), TextAttribute("")]
    public string situation;
    [JsonProperty("cooperates"), ReferenceAttribute(typeof(Institution), true)]
    public string cooperates;
    [JsonProperty("competition"), ReferenceAttribute(typeof(Institution), true)]
    public string competition;
    [JsonProperty("constructs"), ReferenceAttribute(typeof(Construct), true)]
    public string constructs;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
}
