using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Construct : Element
{
    [JsonProperty("rationale"), TextAttribute("")]
    public string rationale;
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("reach"), TextAttribute("")]
    public string reach;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("founder"), ReferenceAttribute(typeof(Character))]
    public string founder;
    [JsonProperty("custodian"), ReferenceAttribute(typeof(Institution))]
    public string custodian;
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
    [JsonProperty("events"), ReferenceAttribute(typeof(Event), true)]
    public string events;
    [JsonProperty("narratives"), ReferenceAttribute(typeof(Narrative), true)]
    public string narratives;
}
