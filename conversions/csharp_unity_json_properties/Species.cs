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
    [JsonProperty("average_weight"), Integer(0)]
    public int averageWeight;
    [JsonProperty("nourishment"), ReferenceAttribute(typeof(Species), true)]
    public string nourishment;
    [JsonProperty("instincts"), TextAttribute("")]
    public string instincts;
    [JsonProperty("aggression"), Integer(100)]
    public int aggression;
    [JsonProperty("agency"), TextAttribute("")]
    public string agency;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("impact"), TextAttribute("")]
    public string impact;
    [JsonProperty("habitat"), ReferenceAttribute(typeof(Location), true)]
    public string habitat;
    [JsonProperty("interaction"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string interaction;
    [JsonProperty("consumables"), ReferenceAttribute(typeof(Construct), true)]
    public string consumables;
}
