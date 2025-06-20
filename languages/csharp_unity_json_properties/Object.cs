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
    [JsonProperty("materials"), ReferenceAttribute(typeof(Construct), true)]
    public string materials;
    [JsonProperty("technology"), ReferenceAttribute(typeof(Construct), true)]
    public string technology;
    [JsonProperty("utility"), TextAttribute("")]
    public string utility;
    [JsonProperty("effects"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string effects;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("consumes"), ReferenceAttribute(typeof(Construct), true)]
    public string consumes;
    [JsonProperty("origins"), TextAttribute("")]
    public string origins;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("language"), ReferenceAttribute(typeof(Language))]
    public string language;
    [JsonProperty("affinities"), ReferenceAttribute(typeof(Trait), true)]
    public string affinities;
}
