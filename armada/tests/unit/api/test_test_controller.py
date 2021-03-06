# Copyright 2017 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from armada.common.policies import base as policy_base
from armada.tests import test_utils
from armada.tests.unit.api import base


class TestControllerNegativeRbacTest(base.BaseControllerTest):

    @test_utils.attr(type=['negative'])
    def test_test_release_insufficient_permissions(self):
        """Tests the GET /api/v1.0/test/{release} endpoint returns 403
        following failed authorization.
        """
        rules = {'armada:test_release': policy_base.RULE_ADMIN_REQUIRED}
        self.policy.set_rules(rules)
        resp = self.app.simulate_get('/api/v1.0/test/test-release')
        self.assertEqual(403, resp.status_code)

    @test_utils.attr(type=['negative'])
    def test_tests_manifest_insufficient_permissions(self):
        """Tests the POST /api/v1.0/tests endpoint returns 403 following failed
        authorization.
        """
        rules = {'armada:tests_manifest': policy_base.RULE_ADMIN_REQUIRED}
        self.policy.set_rules(rules)
        resp = self.app.simulate_post('/api/v1.0/tests')
        self.assertEqual(403, resp.status_code)
