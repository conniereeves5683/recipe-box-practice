# Security baseline

- 2026-11-10: Anonymous **GET /recipes** returns all recipes, including ones with `"is_public": false`.
- 2026-11-10: Anonymous **PATCH /recipes/1** successfully changes the recipe title and returns `200 OK`.
- 2026-11-10: Anonymous **DELETE /recipes/2** returns `204 NO CONTENT`, and **GET /recipes/2** then returns `404 NOT FOUND`.