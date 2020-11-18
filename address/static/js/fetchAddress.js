"use-strict";

const country_select = document.getElementById("id_country");
let country_last_value;

const province_select = document.getElementById("id_province");
let province_last_value;

const district_select = document.getElementById("id_district");
let district_last_value;

const municipality_select = document.getElementById("id_municipality");
let municipality_last_value;

const ward_select = document.getElementById("id_ward");
let ward_last_value;

const helper = async (name, cause, effect, last_value, callback) => {
  const cause_id = cause.value;
  if (cause_id === "") return;

  const raw_response = await fetch(`/address/${name}/${cause_id}`);
  const response = await raw_response.json();
  const data = response.data;

  if (data.length) {
    const current_value = data[0][0];
    // Since id is never repeated, this can be done
    if (last_value && last_value == current_value) return;
    last_value = current_value;
  }

  while (effect.firstChild) {
    effect.lastChild.remove();
  }
  data.forEach(([value, name]) => {
    const option = document.createElement("option");
    option.value = value;
    option.innerText = name;
    effect.appendChild(option);
  });
  callback && callback();
};

country_select.onchange = () => {
  helper(
    "country",
    country_select,
    province_select,
    country_last_value,
    getDistricts
  );
};

const getDistricts = () => {
  helper(
    "province",
    province_select,
    district_select,
    district_last_value,
    getMunicipalities
  );
};

const getMunicipalities = () => {
  helper(
    "district",
    district_select,
    municipality_select,
    municipality_last_value,
    getWards
  );
};

const getWards = () => {
  helper("municipality", municipality_select, ward_select, ward_last_value);
};

province_select.onchange = getDistricts;
district_select.onchange = getMunicipalities;
municipality_select.onchange = getWards;
