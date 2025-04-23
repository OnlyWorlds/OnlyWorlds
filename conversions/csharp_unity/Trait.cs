using System;
using System.Collections.Generic;
[System.Serializable]
public class Trait : BaseElement
{
    // Qualitative
    public string SocialEffects;
    public string PhysicalEffects;
    public string SkillEffects;
    public string PersonalityEffects;
    public string ArtisticEffects;
    public string BehaviourEffects;
    // Quantitative
    public int? Charisma;
    public int? Coercion;
    public int? Capability;
    public int? Compassion;
    public int? Creativity;
    public int? Courage;
    // World
    public string AntiTraitId;
    public List<string> EmpoweredAbilitiesIds; = new List<string>();
}
