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
    [JsonProperty("functional_effects"), TextAttribute("")]
    public string functionalEffects;
    [JsonProperty("personality_effects"), TextAttribute("")]
    public string personalityEffects;
    [JsonProperty("behaviour_effects"), TextAttribute("")]
    public string behaviourEffects;
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
    [JsonProperty("significance"), TextAttribute("")]
    public string significance;
    [JsonProperty("anti_trait"), ReferenceAttribute(typeof(Trait))]
    public string antiTrait;
    [JsonProperty("empowered_abilities"), ReferenceAttribute(typeof(Ability), true)]
    public string empoweredAbilities;
}
