"use-strict";

const country_permanent_select = document.getElementById("id_permanent-country");
let country_permanent_last_value;

const province_permanent_select = document.getElementById("id_permanent-province");
let province_permanent_last_value;

const district_permanent_select = document.getElementById("id_permanent-district");
let district_permanent_last_value;

const municipality_permanent_select = document.getElementById("id_permanent-municipality");
let municipality_permanent_last_value;

const ward_permanent_select = document.getElementById("id_permanent-ward");
let ward_permanent_last_value;

const permaHelper = async (name, cause, effect, last_value, callback) => {
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

country_permanent_select.onchange = () => {
  permaHelper(
    "country",
    country_permanent_select,
    province_permanent_select,
    country_permanent_last_value,
    getPermaDistricts
  );
};

const getPermaDistricts = () => {
  permaHelper(
    "province",
    province_permanent_select,
    district_permanent_select,
    district_permanent_last_value,
    getPermaMunicipalities
  );
};

const getPermaMunicipalities = () => {
  permaHelper(
    "district",
    district_permanent_select,
    municipality_permanent_select,
    municipality_permanent_last_value,
    getPermaWards
  );
};

const getPermaWards = () => {
  permaHelper("municipality", municipality_permanent_select, ward_permanent_select, ward_permanent_last_value);
};

province_permanent_select.onchange = getPermaDistricts;
district_permanent_select.onchange = getPermaMunicipalities;
municipality_permanent_select.onchange = getPermaWards;
