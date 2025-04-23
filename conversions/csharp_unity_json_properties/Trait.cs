using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Trait : Element
{
    [JsonProperty("social_effects"), TextAttribute("")]
    public string socialEffects;
    [JsonProperty("physical_effects"), TextAttribute("")]
    public string physicalEffects;
    [JsonProperty("skill_effects"), TextAttribute("")]
    public string skillEffects;
    [JsonProperty("personality_effects"), TextAttribute("")]
    public string personalityEffects;
    [JsonProperty("artistic_effects"), TextAttribute("")]
    public string artisticEffects;
    [JsonProperty("behaviour_effects"), TextAttribute("")]
    public string behaviourEffects;
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
    [JsonProperty("anti_trait"), ReferenceAttribute(typeof(Trait))]
    public string antiTrait;
    [JsonProperty("empowered_abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string empoweredAbilities;
}
