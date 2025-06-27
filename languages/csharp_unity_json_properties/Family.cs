using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Family : Element
{
    [JsonProperty("spirit"), TextAttribute("")]
    public string spirit;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("traditions"), ReferenceAttribute(typeof(Construct), true)]
    public string traditions;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("ancestors"), ReferenceAttribute(typeof(Character), true)]
    public string ancestors;
    [JsonProperty("reputation"), TextAttribute("")]
    public string reputation;
    [JsonProperty("estates"), ReferenceAttribute(typeof(Location), true)]
    public string estates;
    [JsonProperty("governs"), ReferenceAttribute(typeof(Institution), true)]
    public string governs;
    [JsonProperty("heirlooms"), ReferenceAttribute(typeof(Object), true)]
    public string heirlooms;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
}
