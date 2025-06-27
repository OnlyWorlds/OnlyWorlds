using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Character : Element
{
    [JsonProperty("physicality"), TextAttribute("")]
    public string physicality;
    [JsonProperty("mentality"), TextAttribute("")]
    public string mentality;
    [JsonProperty("height"), Integer(0)]
    public int height;
    [JsonProperty("weight"), Integer(0)]
    public int weight;
    [JsonProperty("species"), ReferenceAttribute(typeof(Species), true)]
    public string species;
    [JsonProperty("traits"), ReferenceAttribute(typeof(Trait), true)]
    public string traits;
    [JsonProperty("abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string abilities;
    [JsonProperty("background"), TextAttribute("")]
    public string background;
    [JsonProperty("motivations"), TextAttribute("")]
    public string motivations;
    [JsonProperty("birth_date"), Integer(0)]
    public int birthDate;
    [JsonProperty("birthplace"), ReferenceAttribute(typeof(Location))]
    public string birthplace;
    [JsonProperty("languages"), ReferenceAttribute(typeof(Language), true)]
    public string languages;
    [JsonProperty("reputation"), TextAttribute("")]
    public string reputation;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("institutions"), ReferenceAttribute(typeof(Institution), true)]
    public string institutions;
    [JsonProperty("charisma"), Integer(100)]
    public int charisma;
    [JsonProperty("coercion"), Integer(100)]
    public int coercion;
    [JsonProperty("competence"), Integer(100)]
    public int competence;
    [JsonProperty("compassion"), Integer(100)]
    public int compassion;
    [JsonProperty("creativity"), Integer(100)]
    public int creativity;
    [JsonProperty("courage"), Integer(100)]
    public int courage;
    [JsonProperty("family"), ReferenceAttribute(typeof(Family), true)]
    public string family;
    [JsonProperty("friends"), ReferenceAttribute(typeof(Character), true)]
    public string friends;
    [JsonProperty("rivals"), ReferenceAttribute(typeof(Character), true)]
    public string rivals;
    [JsonProperty("level"), Integer(0)]
    public int level;
    [JsonProperty("hit_points"), Integer(0)]
    public int hitPoints;
    [JsonProperty("STR"), Integer(0)]
    public int sTR;
    [JsonProperty("DEX"), Integer(0)]
    public int dEX;
    [JsonProperty("CON"), Integer(0)]
    public int cON;
    [JsonProperty("INT"), Integer(0)]
    public int iNT;
    [JsonProperty("WIS"), Integer(0)]
    public int wIS;
    [JsonProperty("CHA"), Integer(0)]
    public int cHA;
}
