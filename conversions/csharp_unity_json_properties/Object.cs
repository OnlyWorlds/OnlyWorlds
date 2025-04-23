using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Object : Element
{
    [JsonProperty("aesthetics"), TextAttribute("")]
    public string aesthetics;
    [JsonProperty("weight"), Integer(0)]
    public int weight;
    [JsonProperty("amount"), Integer(0)]
    public int amount;
    [JsonProperty("parent_object"), ReferenceAttribute(typeof(Object))]
    public string parentObject;
    [JsonProperty("technology"), ReferenceAttribute(typeof(Construct), true)]
    public string technology;
    [JsonProperty("utility"), TextAttribute("")]
    public string utility;
    [JsonProperty("effects"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string effects;
    [JsonProperty("enables"), ReferenceAttribute(typeof(Ability), true)]
    public string enables;
    [JsonProperty("consumes"), ReferenceAttribute(typeof(Construct), true)]
    public string consumes;
    [JsonProperty("origins"), TextAttribute("")]
    public string origins;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("craftsmanship"), TextAttribute("")]
    public string craftsmanship;
    [JsonProperty("requirements"), TextAttribute("")]
    public string requirements;
    [JsonProperty("durability"), TextAttribute("")]
    public string durability;
    [JsonProperty("value"), Integer(0)]
    public int value;
    [JsonProperty("damage"), Integer(0)]
    public int damage;
    [JsonProperty("armor"), Integer(0)]
    public int armor;
    [JsonProperty("rarity"), TextAttribute("")]
    public string rarity;
    [JsonProperty("language"), ReferenceAttribute(typeof(Language))]
    public string language;
    [JsonProperty("requires"), ReferenceAttribute(typeof(Trait), true)]
    public string requires;
}
