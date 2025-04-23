using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Relation : Element
{
    [JsonProperty("history"), TextAttribute("")]
    public string history;
    [JsonProperty("impact"), TextAttribute("")]
    public string impact;
    [JsonProperty("start_date"), Integer(0)]
    public int startDate;
    [JsonProperty("end_date"), Integer(0)]
    public int endDate;
    [JsonProperty("debt"), Integer(0)]
    public int debt;
    [JsonProperty("events"), ReferenceAttribute(typeof(Event), true)]
    public string events;
    [JsonProperty("primary_character"), ReferenceAttribute(typeof(Character))]
    public string primaryCharacter;
    [JsonProperty("primary_creature"), ReferenceAttribute(typeof(Creature))]
    public string primaryCreature;
    [JsonProperty("primary_institution"), ReferenceAttribute(typeof(Institution))]
    public string primaryInstitution;
    [JsonProperty("secondary_characters"), ReferenceAttribute(typeof(Character), true)]
    public string secondaryCharacters;
    [JsonProperty("secondary_creatures"), ReferenceAttribute(typeof(Creature), true)]
    public string secondaryCreatures;
    [JsonProperty("secondary_institutions"), ReferenceAttribute(typeof(Institution), true)]
    public string secondaryInstitutions;
}
