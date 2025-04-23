using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Family : Element
{
    [JsonProperty("spirit"), TextAttribute("")]
    public string spirit;
    [JsonProperty("alliances"), ReferenceAttribute(typeof(Family), true)]
    public string alliances;
    [JsonProperty("rivalries"), ReferenceAttribute(typeof(Family), true)]
    public string rivalries;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("ancestors"), ReferenceAttribute(typeof(Character), true)]
    public string ancestors;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("competition"), ReferenceAttribute(typeof(Institution), true)]
    public string competition;
    [JsonProperty("administrates"), ReferenceAttribute(typeof(Institution), true)]
    public string administrates;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("traditions"), TextAttribute("")]
    public string traditions;
    [JsonProperty("estate"), ReferenceAttribute(typeof(Location))]
    public string estate;
    [JsonProperty("heirlooms"), ReferenceAttribute(typeof(Object), true)]
    public string heirlooms;
}
