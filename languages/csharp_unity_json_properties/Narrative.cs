using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Narrative : Element
{
    [JsonProperty("story"), TextAttribute("")]
    public string story;
    [JsonProperty("consequences"), TextAttribute("")]
    public string consequences;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("order"), Integer(0)]
    public int order;
    [JsonProperty("parent_narrative"), ReferenceAttribute(typeof(Narrative))]
    public string parentNarrative;
    [JsonProperty("protagonist"), ReferenceAttribute(typeof(Character))]
    public string protagonist;
    [JsonProperty("antagonist"), ReferenceAttribute(typeof(Character))]
    public string antagonist;
    [JsonProperty("narrator"), ReferenceAttribute(typeof(Character))]
    public string narrator;
    [JsonProperty("conservator"), ReferenceAttribute(typeof(Institution))]
    public string conservator;
    [JsonProperty("events"), ReferenceAttribute(typeof(Event), true)]
    public string events;
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
    [JsonProperty("laws"), ReferenceAttribute(typeof(Law), true)]
    public string laws;
}
