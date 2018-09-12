# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:38:51 2018

@author: Matthew Wolf
"""
usaid_contracts_fields = ['award_id_piid','award_description','federal_action_obligation','current_total_value_of_award','base_and_all_options_value','potential_total_value_of_award','period_of_performance_start_date',\
                                'period_of_performance_current_end_date','period_of_performance_potential_end_date','action_date','awarding_agency_name',\
                                'awarding_sub_agency_name','awarding_office_name','funding_agency_name','funding_sub_agency_name','funding_office_name','foreign_funding',\
                                'foreign_funding_description','recipient_duns','recipient_name','recipient_parent_name','recipient_parent_duns',\
                                'recipient_country_name','recipient_city_name','recipient_state_name','recipient_zip_4_code','primary_place_of_performance_country_name',\
                                'primary_place_of_performance_city_name','primary_place_of_performance_state_name','award_type','idv_type',\
                                'multiple_or_single_award_idv','type_of_idc','type_of_contract_pricing','award_description','action_type','solicitation_identifier',\
                                'product_or_service_code','product_or_service_code_description','naics_code','naics_description','domestic_or_foreign_entity',\
                                'information_technology_commercial_item_category','epa_designated_product','country_of_product_or_service_origin',\
                                'place_of_manufacture','subcontracting_plan','extent_competed','solicitation_procedures','type_of_set_aside','evaluated_preference',\
                                'number_of_offers_received','a76_fair_act_action','fed_biz_opps','local_area_set_aside','clinger_cohen_act_planning',\
                                'interagency_contracting_authority','major_program','national_interest_action','performance_based_service_acquisition',\
                                'multi_year_contract','contingency_humanitarian_or_peacekeeping_operation','woman_owned_business','women_owned_small_business',\
                                'economically_disadvantaged_women_owned_small_business','joint_venture_women_owned_small_business',\
                                'joint_venture_economic_disadvantaged_women_owned_small_bus','minority_owned_business','subcontinent_asian_asian_indian_american_owned_business',\
                                'asian_pacific_american_owned_business','black_american_owned_business','hispanic_american_owned_business',\
                                'native_american_owned_business','other_minority_owned_business','contracting_officers_determination_of_business_size',\
                                'emerging_small_business','foreign_government','organizational_type','corporate_entity_not_tax_exempt','corporate_entity_tax_exempt',\
                                'partnership_or_limited_liability_partnership','sole_proprietorship','small_agricultural_cooperative','international_organization',\
                                'us_government_entity','community_development_corporation','domestic_shelter','educational_institution','foundation','hospital_flag',\
                                'manufacturer_of_goods','veterinary_hospital','hispanic_servicing_institution','receives_contracts','receives_grants','receives_contracts_and_grants',\
                                'airport_authority','council_of_governments','housing_authorities_public_tribal','interstate_entity','planning_commission',\
                                'port_authority','transit_authority','subchapter_scorporation','limited_liability_corporation','foreign_owned_and_located','for_profit_organization',\
                                'nonprofit_organization','other_not_for_profit_organization','the_ability_one_program','number_of_employees','annual_revenue',\
                                'private_university_or_college','state_controlled_institution_of_higher_learning','last_modified_date',\
                                'award_or_idv_flag']

usaid_assistance_fields = ['award_id_uri','award_description','federal_action_obligation','non_federal_funding_amount','face_value_of_loan',\
                            'total_subsidy_cost','action_date','period_of_performance_start_date','period_of_performance_current_end_date',\
                            'recipient_duns','recipient_name','recipient_parent_name','recipient_parent_duns','recipient_country_name',\
                            'primary_place_of_performance_country_name','cfda_title','assistance_type_code']

usaid_contracts_subs_fields = ['prime_award_piid','subaward_number','subaward_amount','subaward_action_date','prime_awarding_office_name',\
                                'prime_award_principal_place_country','prime_awardee_duns','prime_awardee_name','subawardee_duns',\
                                'subawardee_name','subaward_primary_place_of_performance_country_code','subaward_description',\
                                'subaward_naics_code','subaward_naics_description']

usaid_assistance_subs_fields = ['prime_award_fain','subaward_number','subaward_amount','subaward_action_date',\
                                 'prime_award_principal_place_country','prime_awardee_duns','prime_awardee_name','subawardee_duns',\
                                 'subawardee_name','subaward_primary_place_of_performance_country_code','subaward_description',\
                                 'subaward_cfda_title','subawardee_business_type_description',]

primes_fields = ['award_id','award_description','federal_action_obligation','action_date','period_of_performance_start_date','period_of_performance_current_end_date',\
                 'recipient_duns','recipient_name','recipient_parent_name','recipient_parent_duns','recipient_country_name',\
                 'primary_place_of_performance_country_name']

subs_fields = ['award_id','subaward_number','subaward_amount','subaward_action_date','prime_award_principal_place_country','prime_awardee_duns',\
               'prime_awardee_name','subawardee_duns','subawardee_name','subaward_primary_place_of_performance_country_code','subaward_description']

'''


usaid_contracts_bad_columns = ['multiple_or_single_award_idv_code','idv_type_code','award_type_code','modification_number','transaction_number','parent_award_agency_id','parent_award_agency_name','parent_award_id',\
                               'parent_award_modification_number','base_and_exercised_options_value',\
                               'ordering_period_end_date','awarding_agency_code','awarding_sub_agency_code',\
                               'awarding_office_code','funding_agency_code','funding_sub_agency_code','funding_office_code','sam_exception',\
                               'sam_exception_description','recipient_doing_business_as_name','cage_code','recipient_country_code','recipient_address_line_1',\
                               'recipient_address_line_2','recipient_state_code','recipient_congressional_district','recipient_phone_number',\
                               'recipient_fax_number','primary_place_of_performance_country_code','primary_place_of_performance_county_name',\
                               'primary_place_of_performance_state_code','primary_place_of_performance_zip_4','primary_place_of_performance_congressional_district',\
                               'type_of_idc_code',\
                               'type_of_contract_pricing_code','action_type_code','number_of_actions','contract_bundling_code','contract_bundling',\
                               'recovered_materials_sustainability_code','recovered_materials_sustainability','domestic_or_foreign_entity_code',\
                               'information_technology_commercial_item_category_code','epa_designated_product_code','country_of_product_or_service_origin_code',\
                               'place_of_manufacture_code','subcontracting_plan_code','extent_competed_code','solicitation_procedures_code',\
                               'type_of_set_aside_code','evaluated_preference_code','research_code','research','fair_opportunity_limited_sources_code',\
                               'fair_opportunity_limited_sources','other_than_full_and_open_competition_code','other_than_full_and_open_competition',\
                               'commercial_item_acquisition_procedures_code','commercial_item_acquisition_procedures','small_business_competitiveness_demonstration_program',\
                               'commercial_item_test_program_code','commercial_item_test_program','a76_fair_act_action_code',\
                               'fed_biz_opps_code','local_area_set_aside_code','price_evaluation_adjustment_preference_percent_difference',\
                               'clinger_cohen_act_planning_code','materials_supplies_articles_equipment_code','materials_supplies_articles_equipment',\
                               'labor_standards_code','labor_standards','gfe_gfp','construction_wage_rate_requirements_code',\
                               'construction_wage_rate_requirements','interagency_contracting_authority_code','other_statutory_authority','program_acronym',\
                               'parent_award_type_code','parent_award_type','parent_award_single_or_multiple_code','parent_award_single_or_multiple','national_interest_action_code',\
                               'cost_or_pricing_data_code','cost_or_pricing_data','cost_accounting_standards_clause_code','cost_accounting_standards_clause',\
                               'gfe_gfp_code','undefinitized_action_code','undefinitized_action','consolidated_contract_code','consolidated_contract',\
                               'performance_based_service_acquisition_code','multi_year_contract_code','contract_financing_code','contract_financing',\
                               'purchase_card_as_payment_method_code','purchase_card_as_payment_method','contingency_humanitarian_or_peacekeeping_operation_code',\
                               'alaskan_native_owned_corporation_or_firm','american_indian_owned_business','indian_tribe_federally_recognized',\
                               'native_hawaiian_owned_business','tribally_owned_business','veteran_owned_business','service_disabled_veteran_owned_business',\
                               'contracting_officers_determination_of_business_size_code','community_developed_corporation_owned_firm',\
                               'labor_surplus_area_firm','us_federal_government','federally_funded_research_and_development_corp','federal_agency',\
                               'us_state_government','us_local_government','city_local_government','county_local_government','inter_municipal_local_government',\
                               'local_government_owned','municipality_local_government','school_district_local_government','township_local_government',\
                               'us_tribal_government','1862_land_grant_college','1890_land_grant_college','1994_land_grant_college','minority_institution',\
                               'historically_black_college','tribal_college','alaskan_native_servicing_institution','native_hawaiian_servicing_institution','school_of_forestry',\
                               'veterinary_college','dot_certified_disadvantage','self_certified_small_disadvantaged_business','small_disadvantaged_business',\
                               'c8a_program_participant','historically_underutilized_business_zone_hubzone_firm','sba_certified_8a_joint_venture']

other_contracts_fields = ['award_id_piid','current_total_value_of_award','potential_total_value_of_award', \
                          'period_of_performance_start_date','period_of_performance_current_end_date',\
                          'period_of_performance_potential_end_date','awarding_agency_name','awarding_sub_agency_name',\
                          'awarding_office_name','funding_agency_name','funding_sub_agency_name','funding_office_name',\
                          'foreign_funding','recipient_duns','recipient_name','recipient_parent_name',\
                          'recipient_parent_duns','recipient_country_name','recipient_state_name','recipient_zip_4_code',\
                          'primary_place_of_performance_country_name','primary_place_of_performance_city_name',\
                          'award_type','type_of_contract_pricing','award_description',\
                          'product_or_service_code','product_or_service_code_description','naics_code','naics_description',\
                          'domestic_or_foreign_entity','country_of_product_or_service_origin','place_of_manufacture',\
                          'subcontracting_plan','solicitation_procedures','type_of_set_aside','number_of_offers_received']

'''