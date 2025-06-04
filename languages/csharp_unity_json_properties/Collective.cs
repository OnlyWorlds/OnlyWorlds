using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Collective : Element
{
    [JsonProperty("composition"), TextAttribute("")]
    public string composition;
    [JsonProperty("count"), Integer(0)]
    public int count;
    [JsonProperty("formation_date"), Integer(0)]
    public int formationDate;
    [JsonProperty("operator"), ReferenceAttribute(typeof(Institution))]
    public string operator;
    [JsonProperty("equipment"), ReferenceAttribute(typeof(Construct), true)]
    public string equipment;
    [JsonProperty("activity"), TextAttribute("")]
    public string activity;
    [JsonProperty("temperance"), TextAttribute("")]
    public string temperance;
    [JsonProperty("skills"), ReferenceAttribute(typeof(Ability), true)]
    public string skills;
    [JsonProperty("rituals"), ReferenceAttribute(typeof(Construct), true)]
    public string rituals;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("characters"), ReferenceAttribute(typeof(Character), true)]
    public string characters;
    [JsonProperty("creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string creatures;
    [JsonProperty("phenomena"), ReferenceAttribute(typeof(Phenomenon), true)]
    public string phenomena;
}
