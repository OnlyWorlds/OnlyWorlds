using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Character : Element
{
    [JsonProperty("physicality"), TextAttribute("")]
    public string physicality;
    [JsonProperty("psychology"), TextAttribute("")]
    public string psychology;
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
    [JsonProperty("situation"), TextAttribute("")]
    public string situation;
    [JsonProperty("location"), ReferenceAttribute(typeof(Location))]
    public string location;
    [JsonProperty("titles"), ReferenceAttribute(typeof(Title), true)]
    public string titles;
    [JsonProperty("objects"), ReferenceAttribute(typeof(Object), true)]
    public string objects;
    [JsonProperty("institutions"), ReferenceAttribute(typeof(Institution), true)]
    public string institutions;
    [JsonProperty("charisma"), Integer(100)]
    public int charisma;
    [JsonProperty("coercion"), Integer(100)]
    public int coercion;
    [JsonProperty("capability"), Integer(100)]
    public int capability;
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
    [JsonProperty("backstory"), TextAttribute("")]
    public string backstory;
    [JsonProperty("level"), Integer(0)]
    public int level;
    [JsonProperty("power"), Integer(0)]
    public int power;
    [JsonProperty("price"), Integer(0)]
    public int price;
    [JsonProperty("hit_points"), Integer(0)]
    public int hitPoints;
    [JsonProperty("skill_stealth"), Integer(0)]
    public int skillStealth;
    [JsonProperty("tt_str"), Integer(20)]
    public int ttStr;
    [JsonProperty("tt_int"), Integer(20)]
    public int ttInt;
    [JsonProperty("tt_con"), Integer(20)]
    public int ttCon;
    [JsonProperty("tt_dex"), Integer(20)]
    public int ttDex;
    [JsonProperty("tt_wis"), Integer(20)]
    public int ttWis;
    [JsonProperty("tt_cha"), Integer(20)]
    public int ttCha;
    [JsonProperty("class"), TextAttribute("")]
    public string tt_class;
    [JsonProperty("alignment"), TextAttribute("")]
    public string alignment;
    [JsonProperty("equipment"), ReferenceAttribute(typeof(Object), true)]
    public string equipment;
    [JsonProperty("backpack"), ReferenceAttribute(typeof(Object), true)]
    public string backpack;
    [JsonProperty("proficiencies"), ReferenceAttribute(typeof(Construct), true)]
    public string proficiencies;
    [JsonProperty("features"), ReferenceAttribute(typeof(Trait), true)]
    public string features;
    [JsonProperty("spells"), ReferenceAttribute(typeof(Ability), true)]
    public string spells;
    [JsonProperty("inspirations"), ReferenceAttribute(typeof(Construct), true)]
    public string inspirations;
}
