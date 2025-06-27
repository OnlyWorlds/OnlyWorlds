using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Creature : Element
{
    [JsonProperty("appearance"), TextAttribute("")]
    public string appearance;
    [JsonProperty("weight"), Integer(0)]
    public int weight;
    [JsonProperty("height"), Integer(0)]
    public int height;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("habits"), TextAttribute("")]
    public string habits;
    [JsonProperty("demeanor"), TextAttribute("")]
    public string demeanor;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("status"), TextAttribute("")]
    public string status;
    [JsonProperty("birth_date"), Integer(0)]
    public int birthDate;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("zone"), ReferenceAttribute(typeof(Zone))]
    public string zone;
    [JsonProperty("challenge_rating"), Integer(0)]
    public int challengeRating;
    [JsonProperty("hit_points"), Integer(0)]
    public int hitPoints;
    [JsonProperty("armor_class"), Integer(0)]
    public int armorClass;
    [JsonProperty("speed"), Integer(0)]
    public int speed;
    [JsonProperty("actions"), ReferenceAttribute(typeof(Ability), true)]
    public string actions;
}
