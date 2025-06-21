using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Species : Element
{
    [JsonProperty("appearance"), TextAttribute("")]
    public string appearance;
    [JsonProperty("life_span"), Integer(0)]
    public int lifeSpan;
    [JsonProperty("weight"), Integer(0)]
    public int weight;
    [JsonProperty("nourishment"), ReferenceAttribute(typeof(Species), true)]
    public string nourishment;
    [JsonProperty("reproduction"), ReferenceAttribute(typeof(Construct), true)]
    public string reproduction;
    [JsonProperty("adaptations"), ReferenceAttribute(typeof(Ability), true)]
    public string adaptations;
    [JsonProperty("instincts"), TextAttribute("")]
    public string instincts;
    [JsonProperty("sociality"), TextAttribute("")]
    public string sociality;
    [JsonProperty("temperament"), TextAttribute("")]
    public string temperament;
    [JsonProperty("communication"), TextAttribute("")]
    public string communication;
    [JsonProperty("aggression"), Integer(100)]
    public int aggression;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("role"), TextAttribute("")]
    public string role;
    [JsonProperty("parent_species"), ReferenceAttribute(typeof(Species))]
    public string parentSpecies;
    [JsonProperty("locations"), ReferenceAttribute(typeof(Location), true)]
    public string locations;
    [JsonProperty("zones"), ReferenceAttribute(typeof(Zone), true)]
    public string zones;
    [JsonProperty("affinities"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string affinities;
}
