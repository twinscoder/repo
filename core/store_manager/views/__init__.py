from .stores import (
    StoreAjaxPagination,
    StoreCreateView,
    StoreDeleteView,
    StoreListView,
    StoreUpdateView,
)
from .category import (
    CategoryAjaxPagination,
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryUpdateView,
    SubCategoryAjaxPagination,
    SubCategoryCreateView,
    SubCategoryDeleteView,
    SubCategoryListView,
    SubCategoryUpdateView,
)
from .charges import (
    DeliveryChargeAjaxPagination,
    DeliveryChargeCreateView,
    DeliveryChargeDeleteView,
    DeliveryChargeListView,
    DeliveryChargeUpdateView,
)
from .coupons import (
    CouponAjaxPagination,
    CouponCreateView,
    CouponDeleteView,
    CouponListView,
    CouponUpdateView,
)
from .expenses import (
    ExpenseAjaxPagination,
    ExpenseCreateView,
    ExpenseDeleteView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseTypeAjaxPagination,
    ExpenseTypeCreateView,
    ExpenseTypeDeleteView,
    ExpenseTypeListView,
    ExpenseTypeUpdateView,
)
from .plans import (
    PlanAjaxPagination,
    PlanCreateView,
    PlanDeleteView,
    PlanListView,
    PlanUpdateView,
)
from .products import (
    ProductAjaxPagination,
    ProductCreateView,
    ProductDeleteView,
    ProductListView,
    ProductUpdateView,
    StoreProductAjaxPagination,
    StoreProductCreateView,
    StoreProductDeleteView,
    StoreProductListView,
    StoreProductUpdateView,
)
from .orders import (
    OrderAjaxPagination,
    OrderCreateView,
    OrderDeleteView,
    OrderListView,
    OrderUpdateView,
)
