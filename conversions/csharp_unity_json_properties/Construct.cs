using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Construct : Element
{
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("understanding"), TextAttribute("")]
    public string understanding;
    [JsonProperty("state"), TextAttribute("")]
    public string state;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("founder"), ReferenceAttribute(typeof(Character))]
    public string founder;
    [JsonProperty("organiser"), ReferenceAttribute(typeof(Institution))]
    public string organiser;
    [JsonProperty("characters"), ReferenceAttribute(typeof(Character), true)]
    public string characters;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("locations"), ReferenceAttribute(typeof(Location), true)]
    public string locations;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("institutions"), ReferenceAttribute(typeof(Institution), true)]
    public string institutions;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("collectives"), ReferenceAttribute(typeof(Collective), true)]
    public string collectives;
    [JsonProperty("territories"), ReferenceAttribute(typeof(Territory), true)]
    public string territories;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("families"), ReferenceAttribute(typeof(Family), true)]
    public string families;
    [JsonProperty("relations"), ReferenceAttribute(typeof(Relation), true)]
    public string relations;
    [JsonProperty("titles"), ReferenceAttribute(typeof(Title), true)]
    public string titles;
    [JsonProperty("constructs"), ReferenceAttribute(typeof(Construct), true)]
    public string constructs;
}
