using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Title : Element
{
    [JsonProperty("authority"), TextAttribute("")]
    public string authority;
    [JsonProperty("eligibility"), TextAttribute("")]
    public string eligibility;
    [JsonProperty("grant_date"), Integer(0)]
    public int grantDate;
    [JsonProperty("revoke_date"), Integer(0)]
    public int revokeDate;
    [JsonProperty("issuer"), ReferenceAttribute(typeof(Institution))]
    public string issuer;
    [JsonProperty("body"), ReferenceAttribute(typeof(Institution))]
    public string body;
    [JsonProperty("superior_title"), ReferenceAttribute(typeof(Title))]
    public string superiorTitle;
    [JsonProperty("holders"), ReferenceAttribute(typeof(Character), true)]
    public string holders;
    [JsonProperty("symbols"), ReferenceAttribute(typeof(Object), true)]
    public string symbols;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("characters"), ReferenceAttribute(typeof(Character), true)]
    public string characters;
    [JsonProperty("institutions"), ReferenceAttribute(typeof(Institution), true)]
    public string institutions;
    [JsonProperty("families"), ReferenceAttribute(typeof(Family), true)]
    public string families;
    [JsonProperty("zones"), ReferenceAttribute(typeof(Zone), true)]
    public string zones;
    [JsonProperty("locations"), ReferenceAttribute(typeof(Location), true)]
    public string locations;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("constructs"), ReferenceAttribute(typeof(Construct), true)]
    public string constructs;
    [JsonProperty("laws"), ReferenceAttribute(typeof(Law), true)]
    public string laws;
    [JsonProperty("collectives"), ReferenceAttribute(typeof(Collective), true)]
    public string collectives;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
}
