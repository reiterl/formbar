% if field.is_readonly():
  <div class="readonlyfield" name="${field.name}">
    ${field.get_value(expand=True) or "&nbsp;"}
  </div>
% else:
  <select id="${field.id}" name="${field.name}">
    % for option in field.get_options():
      <option value="${option[1]}">${option[0]}</option>
    % endfor
  </select>
% endif
